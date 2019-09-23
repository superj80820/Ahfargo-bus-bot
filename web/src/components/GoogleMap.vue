<template>
  <b-modal id="modalId" title="地圖" size="xl">
    <GmapMap :center="center" :zoom="12" style="width:inherit; height: 600px">
      <GmapMarker
        :key="index"
        v-for="(m, index) in markers[Direction]"
        :position="m.StopPosition"
        :clickable="true"
        @click="center = m.StopPosition"
      />
      <GmapPolyline :path="pathProp" />
    </GmapMap>
  </b-modal>
</template>

<script>
export default {
  data() {
    return {};
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
    }
  }
};
</script>
