<template>
  <div class="search">
    <form>
      <input type="text" placeholder="输入搜索内容..." v-model="searchText" />
      <!-- 阻止表单原本的提交方法 -->
      <button @click.prevent="searchArticles"></button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SearchButton",
  data: function () {
    return {
      searchText: "",
    };
  },
  methods: {
    searchArticles() {
      // 搜索栏为空时返回主页，该功能待考虑
      if (this.searchText === "") {
        this.$router.push({ name: "Home" });
      }

      // 字符串调用方法前记得判空
      let text = this.searchText;
      if (text !== "") {
        text = this.searchText.trim();
        console.log("成功！");
      }
      if (text.charAt(0) !== "") {
        this.$router.push({ name: "Home", query: { search: text } });
        console.log("搜索功能 可行");
      }
    },
  },
};
</script>

<style lang="less" scoped>
.search {
  padding-top: 22px;
}

* {
  box-sizing: border-box;
}

// 搜索框
form {
  position: relative;
  width: 200px;
  margin: 0 auto;
}

input,
button {
  border: none;
  outline: none;
}

input {
  width: 100%;
  height: 35px;
  padding-left: 13px;
  padding-right: 46px;
}

button {
  height: 35px;
  width: 35px;
  cursor: pointer;
  position: absolute;
} 

.search input {
  border: 2px solid @purpleBtn;
  border-radius: 5px;
  background: transparent;
  top: 0;
  right: 0;
}

.search button {
  background-color: @purpleBtn;
  border-radius: 0 5px 5px 0;
  width: 45px;
  top: 0;
  right: 0;
}

.search button:before {
  content: "搜索";
  font-size: 13px;
  color: white;
}
</style>
