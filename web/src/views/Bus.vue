<template>
  <div class="Bus">
    <b-container>
      <b-row align-h="center">
        <b-card class="w-100">
          <b-button-group class="w-100">
            <b-button
              v-for="(btn, idx) in buttons"
              :key="idx"
              :pressed.sync="btn.state"
              variant="primary"
              @click="updateDirection(idx)"
            >
              {{ btn.route }}
            </b-button>
          </b-button-group>
          <b-table
            striped
            hover
            :items="items[this.Direction]"
            :fields="fields"
            tbody-tr-class="trChindMid"
          >
            <template v-slot:cell(EstimateTime)="row">
              <b-button size="sm" class="mr-2" :variant="row.item.color">
                {{ row.item.EstimateTime }}
              </b-button>
            </template>
            <template v-slot:cell(retPlateNumb)="row">
              <div v-for="(item, index) in row.item.retPlateNumb" :key="index">
                {{ item }}
              </div>
            </template>
          </b-table>
        </b-card>
      </b-row>
    </b-container>
    <BusNavBar
      :value="value"
      :title="title"
      :Direction="Direction"
      :markers="markers"
      :pathProp="pathProp"
      :center="center"
      :busPosition="busPosition"
    />
  </div>
</template>

<script>
import BusNavBar from "../components/BusNavBar.vue";
import dataFilter from "../common/data.filter.js";
import helper from "../common/helper.js";
const axios = require("axios");

function _minFormat(min) {
  if (min <= 1) {
    return "進站中";
  } else if (min <= 2) {
    return "將到站";
  } else {
    return min + "分";
  }
}

export default {
  data() {
    return {
      fields: [
        { key: "EstimateTime", label: "到達時間" },
        { key: "StopName", label: "站名" },
        { key: "retPlateNumb", label: "車牌" }
      ],
      items: [null, null],
      buttons: [],
      value: 0,
      sec: 25,
      title: "更新中...",
      RouteID: parseInt(this.$route.query.RouteID, 10),
      Direction: 0,
      markers: [],
      pathProp: [],
      center: {},
      allPlateNumb: [],
      busPosition: []
    };
  },
  components: {
    BusNavBar
  },
  watch: {
    Direction: function() {
      this.buttons = this.buttons.map((item, index) => {
        return Object.assign(
          {},
          item,
          index === this.Direction ? { state: true } : { state: false }
        );
      });
    }
  },
  methods: {
    updateDirection(idx) {
      this.Direction = idx;
    },
    updateEstimatedTimeOfArrival() {
      return axios
        .get(
          `v2/Bus/EstimatedTimeOfArrival/City/Taichung/${this.RouteID}?$filter=RouteID eq '${this.RouteID}'&$orderby=StopSequence asc&$select=StopName,Direction,NextBusTime,EstimateTime,Estimates&$format=JSON`
        )
        .then(response => {
          console.log(response);
          if (response.data.length === 0) {
            return Promise.reject("get empty array");
          }
          let allPlateNumbCatch = [];
          return {
            astimatedTime: [null, null].map((_, idx) => {
              return response.data
                .filter(item => {
                  return item.Direction === idx;
                })
                .map(item => {
                  let StopName, EstimateTime;
                  let allPlateNumb =
                    item.Estimates !== undefined
                      ? item.Estimates.filter(item => item.EstimateTime <= 180)
                          .sort((a, b) => b.EstimateTime - a.EstimateTime)
                          .map(item => item.PlateNumb)
                      : [];
                  let color = undefined;
                  let retPlateNumb = [];
                  StopName = item.StopName.Zh_tw;
                  allPlateNumb.forEach(item => {
                    if (!allPlateNumbCatch.includes(item)) {
                      allPlateNumbCatch.push(item);
                      retPlateNumb.push(item);
                    }
                  });
                  if (item.EstimateTime !== undefined) {
                    EstimateTime = _minFormat(
                      dataFilter.format(item.EstimateTime)
                    );
                    if (item.EstimateTime <= 60) {
                      color = "success";
                    } else if (item.EstimateTime <= 120) {
                      color = "primary";
                    }
                  } else if (item.NextBusTime !== undefined) {
                    EstimateTime = dataFilter.format(item.NextBusTime);
                  } else {
                    EstimateTime = "末班以離駛";
                  }
                  return { EstimateTime, StopName, retPlateNumb, color };
                });
            }),
            allPlateNumb: allPlateNumbCatch
          };
        })
        .catch(error => {
          console.log(error);
          return Promise.reject(error);
        });
    },
    updateShape() {
      return axios
        .get(
          `v2/Bus/Shape/City/Taichung/${this.RouteID}?$select=Geometry,Direction&$filter=RouteID eq '${this.RouteID}'&$orderby=Direction&$format=JSON`
        )
        .then(response => {
          console.log(response.data);
          return response.data[this.Direction].Geometry.match(/\(.+?\)/g)
            .reverse()
            .map(item => {
              return item
                .replace(/\(|\)/g, "")
                .split(",")
                .map(item => {
                  let temp = item.split(" ");
                  return {
                    lng: parseFloat(temp[0]),
                    lat: parseFloat(temp[1])
                  };
                });
            })
            .reduce((acc, val) => acc.concat(val), []);
        })
        .catch(error => {
          console.log(error);
        });
    },
    updateStopOfRoute() {
      return axios
        .get(
          `v2/Bus/StopOfRoute/City/Taichung/${this.RouteID}?$select=Stops,Direction&$filter=RouteID eq '${this.RouteID}'&$orderby=Direction asc&$format=JSON`
        )
        .then(response => {
          console.log(response);
          return response.data.map(item => {
            return item.Stops.map(item => {
              return Object.assign({}, item, {
                StopPosition: {
                  lng: item.StopPosition.PositionLon,
                  lat: item.StopPosition.PositionLat
                }
              });
            });
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    updateButtonTitile() {
      return axios
        .get(
          `v2/Bus/Route/City/Taichung/${this.RouteID}?$filter=RouteID eq '${this.RouteID}'&$select=DepartureStopNameZh,DestinationStopNameZh&$format=JSON`
        )
        .then(response => {
          console.log(response);
          return [
            {
              route: `往:${response.data[0].DestinationStopNameZh}`,
              state: true
            },
            {
              route: `往:${response.data[0].DepartureStopNameZh}`,
              state: false
            }
          ];
        })
        .catch(error => {
          console.log(error);
        });
    },
    updateRealTimeByFrequency() {
      let query = this.allPlateNumb
        .map(item => `PlateNumb eq '${item}'`)
        .join(" or ");
      return axios
        .get(
          `v2/Bus/RealTimeByFrequency/City/Taichung/${this.RouteID}?$select=BusPosition,PlateNumb,Direction&$filter=RouteID eq '${this.RouteID}' and ${query}&$format=JSON`
        )
        .then(response => {
          console.log(response);
          return [null, null].map((_, index) => {
            return response.data
              .filter(item => {
                return item.Direction === index;
              })
              .map(item => {
                return {
                  PlateNumb: item.PlateNumb,
                  BusPosition: {
                    lat: item.BusPosition.PositionLat,
                    lng: item.BusPosition.PositionLon
                  }
                };
              });
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    autoUpdate(...cb) {
      function callUpdateAgain(scope) {
        scope.value += 4;
        setTimeout(() => scope.autoUpdate(...cb), 1000);
      }
      (scope => {
        if (scope.value >= 100) {
          scope.value = 0;
          scope.sec = 25;
          scope.title = "更新中...";
        }
        if (scope.value === 0) {
          let ppromis = [];
          cb.forEach(s => ppromis.push(s.apply()));
          return Promise.all(ppromis).then(() => {
            scope.title = "更新完成！";
            callUpdateAgain(scope);
          });
        }
        if (scope.value % 4 === 0) {
          scope.sec -= 1;
        }
        if (scope.sec <= 23) {
          scope.title = `${scope.sec}秒後更新`;
        }
        callUpdateAgain(scope);
      })(this);
    }
  },
  mounted: function() {
    (scope => {
      scope.updateStopOfRoute().then(function(value) {
        scope.markers = value;
      });
      scope.updateShape().then(function(value) {
        scope.pathProp = value;
        scope.center = value[Math.floor(value.length / 2)];
        console.log(scope.center);
      });
      scope.updateButtonTitile().then(function(value) {
        scope.buttons = value;
      });
      scope.autoUpdate(() => {
        helper
          .retryPomise(10, 100, scope.updateEstimatedTimeOfArrival)
          .then(function(value) {
            scope.items = value.astimatedTime;
            scope.allPlateNumb = value.allPlateNumb;
            scope.updateRealTimeByFrequency().then(function(value) {
              scope.busPosition = value;
            });
          })
          .catch(function(value) {
            console.log(value);
          });
      });
    })(this);
  }
};
</script>

<style lang="less">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.trChindMid > td {
  vertical-align: middle;
}
</style>
