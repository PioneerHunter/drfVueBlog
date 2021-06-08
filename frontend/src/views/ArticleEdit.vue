<template>
  <blog-header></blog-header>

  <div id="article-create">
    <h3>更新文章</h3>
    <form action="">
      <div class="form-ele">
        <span>标题：</span>
        <input type="text" placeholder="输入标题" v-model="title" />
      </div>

      <div class="form-ele">
        <span>分类：</span>
        <span v-for="category in categories" :key="category.id">
          <button
            class="category-btn"
            :style="categoryStyle(category)"
            @click.prevent="chooseCategory(category)"
          >
            {{ category.title }}
          </button>
        </span>
      </div>

      <div class="form-ele">
        <span>标签：</span>
        <input type="text" placeholder="输入标签，用逗号分格" v-model="tags" />
      </div>

      <div class="form-ele">
        <span>正文：</span>
        <textarea
          placeholder="输入正文"
          v-model="body"
          rows="20"
          cols="80"
        ></textarea>
      </div>

      <div class="form-ele">
        <button @click.prevent="submit">提交</button>
      </div>
      <div class="form-ele">
        <button @click.prevent="deleteArticle" style="backgroud-color: darkred">
          删除
        </button>
      </div>
    </form>
  </div>

  <blog-footer></blog-footer>
</template>

<script>
import axios from "axios";
import BlogHeader from "@/components/BlogHeader.vue";
import BlogFooter from "@/components/BlogFooter.vue";
import authorization from "@/utils/authorization";
export default {
  name: "ArticleEdit",
  components: {
    BlogHeader,
    BlogFooter,
  },
  data: function () {
    return {
      title: "",
      body: "",
      categories: [],
      selectedCategory: null,
      tags: "",
    };
  },
  mounted() {
    // 获取所有分类
    axios
      .get("/api/category/")
      .then((response) => (this.categories = response.data));
    const that = this;
    axios
      .get("/api/article/" + that.$route.params.id + "/")
      .then(function (response) {
        const data = response.data;
        that.title = data.title;
        that.body = data.body;
        that.selectedCategory = data.category;
        that.articleID = data.id;
      });
  },
  methods: {
    // 按钮颜色变化
    categoryStyle(category) {
      if (
        this.selectedCategory !== null &&
        category.id === this.selectedCategory.id
      ) {
        return {
          backgroundColor: "black",
        };
      }
      return {
        backgroundColor: "lightgrey",
        color: "black",
      };
    },
    // 选取分类的方法
    chooseCategory(category) {
      if (
        this.selectedCategory !== null &&
        this.selectedCategory.id === category.id
      ) {
        this.selectedCategory = null;
      } else {
        this.selectedCategory = category;
      }
    },
    // 点击提交按钮
    submit() {
      const that = this;
      authorization().then(function (resposne) {
        if (resposne[0]) {
          let data = {
            title: that.title,
            body: that.body,
          };
          data.category_id = that.selectedCategory
            ? that.selectedCategory.id
            : null;

          // 标签预处理
          data.tags = that.tags
            .split(/[,，]/)
            .map((x) => x.trim())
            .filter((x) => x.charAt(0) !== "");
          const token = localStorage.getItem("access.myblog");
          axios
            .put("/api/article/" + that.articleID + "/", data, {
              headers: { Authorization: "Bearer " + token },
            })
            .then(function (response) {
              that.$router.push({
                name: "ArticleDetail",
                params: { id: response.data.id },
              });
            });
        } else {
          alert("令牌过期，请重新登录。");
        }
      });
    },
    deleteArticle() {
      const that = this;
      const token = localStorage.getItem("access.myblog");
      authorization().then(function (response) {
        if (response[0]) {
          axios
            .delete("/api/article/" + that.articleID + "/", {
              headers: { Authorization: "Bearer " + token },
            })
            .then(() => that.$router.push({ name: "Home" }));
        } else {
          alert("令牌过期，请重新登录。");
        }
      });
    },
  },
};
</script>

<style lang="less" scoped>
.category-btn {
  margin-right: 10px;
}
#article-create {
  text-align: center;
  font-size: large;
}
form {
  text-align: left;
  padding-left: 100px;
  padding-right: 10px;
}
.form-ele {
  padding: 10px;
}
input {
  height: 25px;
  padding-left: 10px;
  width: 50%;
}
button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: steelblue;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
</style>
