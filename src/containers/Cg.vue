<template lang="jade">
.cg-list
  cg.cg(v-for="cg in cgs", :cg="cg", key="cg.id")
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Cg from '@/components/Cg';

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.cgs.length) {
      this.getCgs({ page: 1, size: 10 });
    }
  },
  computed: {
    ...mapGetters({
      cgs: 'cgs',
      isFetching: 'isFetching',
    }),
  },
  methods: {
    ...mapActions({
      getCgs: 'getCgs',
    }),
  },
  components: {
    Cg,
  },
};
</script>

<style lang="stylus" scoped>
.cg-list
  margin 1rem
  display flex
  flex-flow row wrap
  justify-content space-between

  .cg
    margin-bottom 2rem
</style>
