<template>
  <div class="fixed-bottom">
    <b-progress :value="value" :max="max" height="5px"></b-progress>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand>{{ title }}</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-b-modal="'modalId'">地圖</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <GoogleMap
      :modalId="modalId"
      :Direction="Direction"
      :markers="markers"
      :pathProp="pathProp"
      :center="center"
    />
  </div>
</template>

<script>
import GoogleMap from "../components/GoogleMap.vue";

export default {
  props: {
    markers: {
      type: Array
    },
    value: {
      type: Number
    },
    title: {
      type: String
    },
    Direction: {
      type: Number
    },
    pathProp: {
      type: Array
    },
    center: {
      type: Object
    }
  },
  data() {
    return {
      max: 100,
      modalId: "map"
    };
  },
  components: {
    GoogleMap
  }
};
</script>
