<template>
  <b-modal
    v-if="showMap"
    id="modalId"
    title="地圖"
    size="xl"
    @hide="$store.commit('changeShowMapModal')"
  >
    <GmapMap :center="center" :zoom="12" style="width:inherit; height: 600px">
      <gmap-custom-marker
        v-for="(item, index) in markers[Direction]"
        :key="item.id"
        :marker="item.StopPosition"
        @click.native="$store.state.mapCenter = item.StopPosition"
      >
        <b-button
          variant="primary"
          class="btn-circle"
          :id="'stop-target-' + index"
        >
          {{ index }}
        </b-button>
        <b-popover
          :target="'stop-target-' + index"
          triggers="focus"
          placement="right"
        >
          <template v-slot:title>
            {{ item.StopName }}
            <b-button size="sm" @click="redirect('table-target-' + index)">
              時刻
            </b-button>
          </template>
        </b-popover>
      </gmap-custom-marker>
      <gmap-custom-marker
        v-for="(item, index) in busPosition[Direction]"
        :key="item.id"
        :marker="item.BusPosition"
        @click.native="$store.state.mapCenter = item.BusPosition"
      >
        <b-button
          variant="success"
          class="btn-circle"
          :id="'bus-target-' + index"
        >
          bus
        </b-button>
        <b-popover
          :target="'bus-target-' + index"
          triggers="focus"
          placement="right"
        >
          <template v-slot:title>
            {{ item.PlateNumb }}
          </template>
        </b-popover>
      </gmap-custom-marker>
      <GmapPolyline :path="pathProp" />
    </GmapMap>
  </b-modal>
</template>

<script>
import GmapCustomMarker from "vue2-gmap-custom-marker";

export default {
  data() {
    return {};
  },
  methods: {
    redirect(id) {
      this.$store.commit("changeShowMapModal");
      var elmnt = document.getElementById(id);
      elmnt.scrollIntoView();
    }
  },
  computed: {
    center() {
      return this.$store.state.mapCenter;
    },
    showMap() {
      return this.$store.state.showMapModal;
    }
  },
  components: {
    "gmap-custom-marker": GmapCustomMarker
  },
  props: {
    markers: {
      type: Array
    },
    Direction: {
      type: Number
    },
    modalId: {
      type: String
    },
    pathProp: {
      type: Array
    },
    busPosition: {
      type: Array
    }
  }
};
/*
CSS btn-circle ref: https://codepen.io/jnbruno/pen/vNpPpW
*/
</script>

<style>
.btn-circle {
  width: 25px;
  height: 25px;
  padding: 3px 0px;
  border-radius: 20px;
  text-align: center;
  font-size: 5px;
  line-height: 1.42857;
}
</style>
