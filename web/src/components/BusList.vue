<template>
  <b-container>
    <b-row align-h="center">
      <b-card class="w-100">
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
    </b-row>
  </b-container>
</template>

<script>
export default {
  props: {
    buttons: {
      type: Array
    },
    items: {
      type: Array
    }
  }
};
</script>
