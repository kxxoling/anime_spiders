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
</style>
