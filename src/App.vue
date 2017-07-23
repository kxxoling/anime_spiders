<template lang="jade">
#app
  header-nav
  router-view.view-container
</template>

<script>
import HeaderNav from '@/components/HeaderNav';
import 'font-awesome/css/font-awesome.css';

export default {
  name: 'app',
  components: {
    HeaderNav,
  },
  metaInfo: {
    title: 'Home',
    titleTemplate: '%s - Spider the anime world',
    htmlAttrs: {
      lang: 'zh-CN',
    },
  },
};
</script>

<style lang="stylus">
figure
  margin 0
  padding 0

.view-container
  display flex
  justify-content space-between
  flex-flow row wrap
  margin 1rem auto
  box-sizing border-box
  padding 0 1rem

@media(min-width: 1024px)
  .view-container
    width 1000px

@media(min-width: 1400px)
  .view-container
    width 1360px

@media(min-width: 1800px)
  .view-container
    width 100%
    padding 0 2rem

// hack el-dialog styles
.el-dialog__wrapper
  height 100%
  width 100%

.el-dialog
  top 10% !important
  height 80% !important
  overflow hidden !important
  margin 0 !important

.el-dialog__header
  display none
.el-dialog__body
  height 100% !important
  box-sizing border-box !important
</style>
