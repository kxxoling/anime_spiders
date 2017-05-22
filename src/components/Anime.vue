<template lang="jade">
.anime
  figure.cover
    img(v-bind:src="anime.cover")
  div.desc
    div
      a(v-bind:href="site_link", target="_blank")
        span {{ anime.name }}
    div(v-if="anime.orig_name")
      label 原名：
      span （{{ anime.orig_name }}）
    div
      label 发布日期：
      span {{ anime. pub_date}}
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
.anime
  height 14rem
  width 24rem
  display flex
  border 1px solid #ccc
  padding 1rem

  .cover
    display flex
    align-items center
  .desc
    margin-left 1rem

    &>div
      margin-bottom 1rem
</style>
