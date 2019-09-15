<template>
  <div class="Bus">
    <BusNavBar :value="value" :sec="sec" />
    <BusList :buttons="buttons" :items="items" />
  </div>
</template>

<script>
import BusNavBar from "../components/BusNavBar.vue";
import BusList from "../components/BusList.vue";

export default {
  data() {
    return {
      value: 0,
      sec: 25,
      buttons: [
        { route: "往:中臺科技大學校區", state: true },
        { route: "往:臺中刑務所演武場", state: false }
      ],
      items: [
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" },
        { 預估到站: "12:30", 站牌: "Larsen", 車號: "A38-3" }
      ]
    };
  },
  components: {
    BusNavBar,
    BusList
  },
  methods: {},
  created: function() {
    setInterval(
      (function(scope) {
        return function() {
          if (scope.value >= 100) {
            scope.value = 0;
            scope.sec = 25;
            console.log("Get API");
          }
          if (scope.value % 4 === 0) {
            scope.sec -= 1;
          }
          scope.value += 1;
        };
      })(this),
      250
    );
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
