<template>
  <b-modal id="modalId" title="地圖" size="xl">
    <GmapMap :center="test" :zoom="12" style="width:inherit; height: 600px">
      <gmap-custom-marker
        v-for="(item, index) in markers[Direction]"
        :key="item.id"
        :marker="item.StopPosition"
        @click.native="test = item.StopPosition"
      >
        <b-button
          variant="primary"
          class="btn-circle"
          :id="'popover-target-' + index"
        >
          {{ index }}
        </b-button>
        <b-popover
          :target="'popover-target-' + index"
          triggers="focus"
          placement="right"
        >
          <template v-slot:title>
            {{ index }}
          </template>
        </b-popover>
      </gmap-custom-marker>
      <gmap-custom-marker
        v-for="(item, index) in busPosition[Direction]"
        :key="item.id"
        :marker="item.BusPosition"
        @click.native="test = item.BusPosition"
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
    return {
      test: {
        lat: 24.1915999996404,
        lng: 120.702489999614
      }
    };
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
    center: {
      type: Object
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
