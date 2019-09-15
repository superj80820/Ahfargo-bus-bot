<template>
  <b-modal id="modalId" title="地圖" size="xl">
    <GmapMap
      :center="{ lat: 10, lng: 10 }"
      :zoom="7"
      style="width:inherit; height: 600px"
    >
    </GmapMap>
  </b-modal>
</template>

<script>
export default {
  props: {
    modalId: {
      type: String
    }
  }
};
</script>
