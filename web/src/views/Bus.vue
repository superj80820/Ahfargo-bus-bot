<template>
  <div class="home">
    <b-container>
      <b-card
      img-src="https://images.sgcafe.net/2014/10/10665212_682477758503582_3260636404939881942_n.jpg"
      img-alt="Image"
      class="p-3"
      >
        <b-button-group class="w-100">
          <b-button
            v-for="(btn, idx) in buttons"
            :key="idx"
            :pressed.sync="btn.state"
            variant="primary"
          >
            {{ btn.route }}
          </b-button>
        </b-button-group>
        <b-table striped hover :items="items"></b-table>
      </b-card>
    </b-container>
    <div></div><div></div><div></div><div></div><div></div><div></div><div></div>
    <vue-live2d
    style="bottom: -20px; width: 1500px; height: 300px; opacity: 1;"
    :modelPath="modelPath"
    :defaultScale="2"
    >
    </vue-live2d>
  </div>
  
</template>

<script>
export default {
  data() {
    return {
      myToggle: false,
      buttons: [
        { route: "往:中臺科技大學校區", state: true },
        { route: "往:臺中刑務所演武場", state: false }
      ],
      items: [
        { 站序: 40, 站牌: 'Dickerson', 編號: 'Macdonald', 預估到站: "12:30"},
        { 站序: 21, 站牌: 'Larsen', 編號: 'Shaw', 預估到站: "12:30"},
        { 站序: 89, 站牌: 'Geneva', 編號: 'Wilson', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"},
        { 站序: 38, 站牌: 'Jami', 編號: 'Carney', 預估到站: "12:30"}
      ],
      modelPath: [
        {
          order: 1,
          path: "/live2d/miku/miku.model.json",
        }
      ]
    };
  },
  methods: {
  }
};
</script>