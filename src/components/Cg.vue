<template lang="jade">
.cg
  figure
    img(v-bind:src="localSrc")
</template>

<script>
export default {
  props: {
    cg: Object,
  },
  data() {
    return {};
  },
  computed: {
    site_link() {
      return `//bangumi.tv${this.anime.link}`;
    },
    localSrc() {
      const localPath = 'donmai_hot';
      const localName = this.cg.large_file_url.split('/').pop();
      return `/storage/${localPath}/${localName}`;
    },
  },
};
</script>

<style lang="stylus" scoped>
.cg
  height 18rem
  width 12rem
  display flex
  padding 1rem
</style>
