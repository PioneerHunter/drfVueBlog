<template>
  <blog-header></blog-header>
  <article-list></article-list>
  <blog-footer></blog-footer>
</template>

<script>
import BlogHeader from "@/components/BlogHeader.vue";
import BlogFooter from "@/components/BlogFooter.vue";
import ArticleList from "@/components/ArticleList.vue";

export default {
  name: "App",
  components: {
    BlogHeader,
    ArticleList,
    BlogFooter,
  },
};
</script>

<style>

</style>
