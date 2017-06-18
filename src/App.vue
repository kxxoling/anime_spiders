<template>
  <div id="app">
    <header-nav/>
    <router-view></router-view>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav';
import 'font-awesome/css/font-awesome.css';

export default {
  name: 'app',
  components: {
    HeaderNav,
  },
};
</script>

<style lang="stylus">
figure
  margin 0
  padding 0

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
