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
              @click="buttonTest(idx)"
            >
              {{ btn.route }}
            </b-button>
          </b-button-group>
          <b-table striped hover :items="items[this.Direction]"></b-table>
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
    />
  </div>
</template>

<script>
import BusNavBar from "../components/BusNavBar.vue";
const axios = require("axios");

export default {
  data() {
    return {
      items: [null, null],
      buttons: [],
      value: 0,
      sec: 25,
      title: "更新中...",
      RouteID: null,
      Direction: 0,
      markers: [],
      pathProp: [],
      center: {}
    };
  },
  components: {
    BusNavBar
  },
  methods: {
    buttonTest(idx) {
      console.log(idx);
      this.Direction = idx;
      this.buttons = this.buttons.map((item, index) => {
        return Object.assign(
          {},
          item,
          index === idx ? { state: true } : { state: false }
        );
      });
    },
    estimatedTimeOfArrival(RouteID) {
      return axios
        .get(
          `v2/Bus/EstimatedTimeOfArrival/City/Taichung/${RouteID}?$filter=RouteID eq '${RouteID}'&$orderby=StopSequence asc&$select=StopName,Direction,NextBusTime,EstimateTime&$format=JSON`
        )
        .then(response => {
          console.log(response);
          this.items = this.items.map((_, idx) => {
            return response.data
              .filter(item => {
                return item.Direction === idx;
              })
              .map(item => {
                return (({ StopSequence, StopName, EstimateTime }) => {
                  StopSequence = item.StopSequence;
                  StopName = item.StopName.Zh_tw;
                  if (item.EstimateTime != undefined) {
                    EstimateTime = item.EstimateTime;
                  } else {
                    EstimateTime = item.NextBusTime;
                  }
                  return { StopSequence, StopName, EstimateTime };
                })(item);
              });
          });
          console.log(this.items);
        })
        .catch(error => {
          console.log(error);
        });
    },
    pathFunc(RouteID) {
      return axios
        .get(
          `v2/Bus/Shape/City/Taichung/${RouteID}?$select=Geometry,Direction&$filter=RouteID eq '${RouteID}'&$orderby=Direction&$format=JSON`
        )
        .then(response => {
          console.log(response.data);
          this.pathProp = response.data[this.Direction].Geometry.match(
            /\(.+?\)/g
          )
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
          this.center = this.pathProp[Math.floor(this.pathProp.length / 2)];
        })
        .catch(error => {
          console.log(error);
        });
    },
    stop(RouteID) {
      return axios
        .get(
          `v2/Bus/StopOfRoute/City/Taichung/${RouteID}?$select=Stops,Direction&$filter=RouteID eq '${RouteID}'&$orderby=Direction asc&$format=JSON`
        )
        .then(response => {
          console.log(response);
          this.markers = response.data.map(item => {
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
    buttonTitile(RouteID) {
      return axios
        .get(
          `v2/Bus/Route/City/Taichung/${RouteID}?$filter=RouteID eq '${RouteID}'&$select=DepartureStopNameZh,DestinationStopNameZh&$format=JSON`
        )
        .then(response => {
          console.log(response);
          this.buttons = [
            {
              route: `往:${response.data[0].DestinationStopNameZh}`,
              state: true
            },
            {
              route: `往:${response.data[0].DepartureStopNameZh}`,
              state: false
            }
          ];
          console.log(this.buttons);
        })
        .catch(error => {
          console.log(error);
        });
    },
    update(...cb) {
      function callUpdateAgain(scope) {
        scope.value += 4;
        setTimeout(() => scope.update(...cb), 1000);
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
  created: function() {
    this.RouteID = this.$route.query.RouteID;
    this.stop(this.RouteID);
    this.pathFunc(this.RouteID);
    this.buttonTitile(this.RouteID);
    this.update(() => this.estimatedTimeOfArrival(this.RouteID));
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
</style>
