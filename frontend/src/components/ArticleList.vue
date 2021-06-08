<template>
  <div id="articles" v-for="article in info.results" v-bind:key="article.url">
    <span class="category" v-if="article.category !== null">
      {{ article.category.title }}
    </span>

    <div class="article-container">
      <router-link
        class="article-title"
        :to="{ name: 'ArticleDetail', params: { id: article.id } }"
      >
        {{ article.title }}
      </router-link>
    </div>

    <div>
      {{ formatted_time(article.created) }}
      <span v-for="tag in article.tags" v-bind:key="tag" class="tag">
        {{ tag }}
      </span>
    </div>
  </div>

  <div id="paginator">
    <span v-if="is_page_exists('previous')">
      <router-link :to="get_path('previous')"> Prev </router-link>
    </span>

    <span class="current-page">
      {{ get_page_param("current") }}
    </span>

    <span v-if="is_page_exists('next')">
      <router-link :to="get_path('next')"> Next </router-link>
    </span>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleList",
  data: function () {
    return {
      info: "",
    };
  },
  watch: {
    // 监听路由是否变化
    $route() {
      this.get_article_data();
    },
  },
  mounted() {
    this.get_article_data();
  },
  methods: {
    // 返回转化的文章创建时间
    formatted_time: function (iso_date_string) {
      const date = new Date(iso_date_string);
      return date.toLocaleDateString();
    },

    // 判断页面是否存在
    is_page_exists: function (direction) {
      if (direction === "next") {
        return this.info.next !== null;
      }
      return this.info.previous !== null;
    },

    // 获取页码
    get_page_param: function (direction) {
      try {
        let url_string;
        switch (direction) {
          case "next":
            url_string = this.info.next;
            break;
          case "previous":
            url_string = this.info.previous;
            break;
          default:
            return this.$route.query.page;
        }
        const url = new URL(url_string);
        return url.searchParams.get("page");
      } catch (err) {
        return "页码出问题";
      }
    },

    // 获取文章列表数据
    get_article_data: function () {
      // eslint-disable-next-line no-unused-vars
      let url = "/api/article";
      // 该对象用于生成和解析url的参数字符串
      let params = new URLSearchParams();
      // 判断值是否存在并添加该值，{ 键名：值 }
      // appendIfExists为自定义方法，详情见src/main.js文件
      params.appendIfExists("page", this.$route.query.page);
      params.appendIfExists("search", this.$route.query.search);

      const paramsString = params.toString();
      if (paramsString.charAt(0) !== "") {
        url += "/?" + paramsString; // 地址拼接
      }
      // 获取后端返回数据，http://127.0.0.1:8000/api/article/?page=.../...
      axios.get(url).then((response) => (this.info = response.data));
    },

    // 获取路径
    get_path: function (direction) {
      let url = "";
      try {
        switch (direction) {
          case "next":
            if (this.info.next !== undefined) {
              url += new URL(this.info.next).search;
            }
            break;
          case "previous":
            if (this.info.previous !== undefined) {
              url += new URL(this.info.previous).search;
            }
            break;
        }
      } catch {
        return console.log("返回路径错误");
      }
      return url;
    },
  },
};
</script>

<style lang="less" scoped>
#articles {
  padding: 20px;
  margin: 5px 50px 5px 50px;
  border: 1px solid #c56bdb;
  line-height: 25px;
  border-radius: 15px;
}

#articles:hover {
  box-shadow: 0 0 15px #888888;
  border-color: @bgc;
}
.article-container {
  padding: 5px 0 5px 0;
}
.article-title {
  font-size: large;
  font-weight: bolder;
  color: black;
  text-decoration: none;
  padding: 5px 0 5px 0;
}
.category {
  padding: 5px 10px 5px 10px;
  margin: 5px 5px 5px 0;
  font-family: Georgia, Arial, sans-serif;
  font-size: small;
  background-color: darkred;
  color: whitesmoke;
  border-radius: 15px;
}
.tag {
  padding: 2px 5px 2px 5px;
  margin: 5px 5px 5px 0;
  font-family: Georgia, Arial, sans-serif;
  font-size: small;
  background-color: #4e4e4e;
  color: whitesmoke;
  border-radius: 5px;
}
#paginator {
  text-align: center;
  padding-top: 50px;
}
a {
  color: black;
}
.current-page {
  font-size: x-large;
  font-weight: bold;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
