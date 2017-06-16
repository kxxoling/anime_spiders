<template lang="jade">
.anime
  figure.cover
    img(v-bind:src="anime.cover")
    figcaption.figcaption
      a(v-bind:href="site_link", target="_blank")
        span {{ anime.name }}
  div.desc
    h3(title="anime.orig_name", alt="anime.orig_name || anime.name") {{ anime.orig_name || anime.name }}
    div.details
      label 发布于：
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
      return `${this.anime.link}`;
    },
  },
};
</script>

<style lang="stylus" scoped>
a
  text-decoration none

.anime
  height 12rem
  width 20rem
  display flex
  border-radius 4px
  box-shadow 0 0 1rem rgba(0, 0, 0, .2)
  overflow hidden

  .cover
    display flex
    align-items center
    position relative
    width 8rem
    height 12rem

    img
      height 100%
      width 100%

    .figcaption
      position absolute
      bottom 0
      width 100%
      text-align center
      background linear-gradient(
        transparent,rgba(0,0,0,0.3) 10%,
        rgba(0,0,0,0.5) 35%,
        rgba(0,0,0,0.7) 65%,
        rgba(0,0,0,0.9)
      )
      padding 0.8rem 0

      a
        color white

  .desc
    flex 1
    margin-left 1rem
    margin-right 1rem

    &>div
      margin-bottom 1rem
      font-size 0.9rem
</style>
