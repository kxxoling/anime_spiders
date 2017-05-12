<template lang="jade">
.anime
  a(v-bind:href="site_link", target="_blank")
    img(v-bind:src="anime.cover")
    span {{ anime.name }}
    span （{{ anime.orig_name }}）
</template>

<script>
export default {
  props: {
    anime: Object,
  },
  data() {
    return {};
  },
  computed: {
    site_link() {
      return `//bangumi.tv${this.anime.link}`;
    },
  },
};
</script>

<style lang="stylus" scoped>

</style>
