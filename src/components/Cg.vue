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
      const localPath = 'danbooru_donmai_us';
      const localName = this.cg.large_file_url.split('/').pop();
      return `/storage/${localPath}/${localName}`;
    },
  },
};
</script>

<style lang="stylus" scoped>
.cg
  height 18rem
  width 15rem
  display flex

  img
    max-width 100%
    max-height 100%

    &:hover
      box-shadow 0 0 2rem #aaa
</style>
