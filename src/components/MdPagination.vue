<template lang="jade">
ul.pagination
  li(:class='{disabled: currentPage == 1}')
    a(v-if='firstLast', @click.prevent='currentPage = 1', href='#')
      i.material-icons chevron_left
    a(@click.prevent='previousPage', href='#')
      i.material-icons chevron_left
  li(
    v-for='n in pager',
    @click='currentChange(n)',
    :class='getClasses(n)'
  )
    a(href='', @click.prevent='') {{ n }}
  li(:class='{disabled: currentPage == pagesCount}')
    a(@click.prevent='nextPage', href='#')
      i.material-icons chevron_right
    a(v-if='firstLast', @click.prevent='currentPage = pagesCount', href='#')
      i.material-icons chevron_right
</template>

<script>
import { mdIcon } from 'vue-material';

function generatePagination(currentPage, pagesCount, displayPages) {
  const pager = [];
  pager.push(currentPage);
  let skip = 1;
  while (pager.length < displayPages && pager.length <= pagesCount) {
    const page = currentPage + skip;
    if (page > 0 && page <= pagesCount) {
      pager.push(page);
    }
    skip = skip > 0 ? skip * -1 : (skip * -1) + 1;
  }
  return pager.sort((n1, n2) => n1 - n2);
}

export default {
  props: {
    currentPage: {
      type: Number,
      required: true,
      twoWay: true,
    },
    itemClass: {
      required: false,
      default: 'waves-effect',
      twoWay: false,
    },
    firstLast: {
      type: Boolean,
      required: false,
      default: false,
      twoWay: false,
    },
    pagesCount: {
      type: Number,
      required: true,
    },
    currentChange: {
      type: Function,
      required: false,
      default: () => {},
    },
  },
  components: {
    mdIcon,
  },
  data() {
    return {
      displayPages: 10,
    };
  },
  computed: {
    pager() {
      return generatePagination(this.currentPage, this.pagesCount, this.displayPages);
    },
  },
  methods: {
    getClasses(n) {
      // return `md-${n}`;
      const classes = {};
      if (this.itemClass instanceof Array) {
        this.itemClass.forEach((value) => {
          classes[value] = true;
        });
      } else if (this.itemClass instanceof Object) {
        this.itemClass.keys().forEach((value) => {
          classes[value] = true;
        });
      } else {
        classes[this.itemClass] = true;
      }
      classes.active = n === this.currentPage;
      return classes;
    },
    setCurrentPage(n) {
      this.currentPage = n;
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentChange(this.currentPage - 1);
      }
    },
    nextPage() {
      if (this.currentPage < this.pagesCount) {
        this.currentChange(this.currentPage + 1);
      }
    },
  },
};
</script>

<style lang="stylus" scoped>
$height = 30px

ul.pagination
  li
    display inline-block
    border-radius 2px
    text-align center
    vertical-align middle
    height $height
    line-height $height
    margin 0

    a
      color #444
      display inline-block
      font-size 1.2rem
      padding 0 10px
      line-height $height
    &.active
      background-color #ee6e73
      a
        color #fff
    &.disabled
      a
        cursor default
        color #999
    i
      font-size 2rem
    &.pages
      ul
        li
          display inline-block
          float none

@media only screen and (max-width: 992px)
  .pagination
    width 100%
    li
      &.pages
        width 80%
        overflow hidden
        white-space nowrap

  .pagination li.prev, .pagination li.next
    width 10%
</style>
