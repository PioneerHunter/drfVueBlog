<template>
  <div id="header">
    <div class="grid">
      <div></div>
      <h1>FoolBird's Blog</h1>

      <search-button></search-button>
    </div>
    <hr />
    <div class="login">
      <div v-if="hasLogin">
        <div class="dropdown">
          <button class="dropbtn">欢迎，{{ username }}!</button>
          <div class="dropdown-content">
            <router-link
              :to="{ name: 'UserCenter', params: { username: username } }"
            >
              用户中心
            </router-link>
            <router-link :to="{ name: 'ArticleCreate' }" v-if="isSuperuser">
              发布文章
            </router-link>
            <!-- 退出登录并返回首页 -->
            <router-link class="logout" @click="logout" to="/">
              Logout
            </router-link>
          </div>
        </div>
      </div>
      <div v-else>
        <router-link class="login-link" to="/login">登录</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import SearchButton from "./SearchButton.vue";
import authorization from "@/utils/authorization.js";

export default {
  name: "BlogHeader",
  components: { SearchButton },
  data: function () {
    return {
      username: "",
      hasLogin: false,
      isSuperuser: JSON.parse(localStorage.getItem("isSuperuser.myblog")),
    };
  },
  mounted() {
    authorization().then((data) => ([this.hasLogin, this.username] = data));
  },
  methods: {
    // 退出登录
    logout() {
      // 清空本地缓存
      localStorage.clear();
      // window.location.reload(false);
    },
    // 更新登录用户名
    refresh() {
      this.username = localStorage.getItem("username.myblog");
    },
  },
};
</script>

<style lang="less" scoped>
// 布局
#header {
  text-align: center;
  padding: 20px;
  background-color: @bgcHeight;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr;
}

// 注册
.login-link {
  color: black;
}

.login {
  text-align: right;
  padding-right: 50px;
}

.dropbtn {
  background-color: mediumslateblue;
  color: white;
  padding: 8px 8px 30px 8px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  height: 16px;
  border-radius: 5px;
}
/* 容器 <div> - 需要定位下拉内容 */
.dropdown {
  position: relative;
  display: inline-block;
}
/* 下拉内容 (默认隐藏) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
}
/* 下拉菜单的链接 */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
/* 鼠标移上去后修改下拉菜单链接颜色 */
.dropdown-content a:hover {
  background-color: #f1f1f1;
}
/* 在鼠标移上去后显示下拉菜单 */
.dropdown:hover .dropdown-content {
  display: block;
}
/* 当下拉内容显示后修改下拉按钮的背景颜色 */
.dropdown:hover .dropbtn {
  background-color: darkslateblue;
}
hr {
  background-color: @bgcHeight;
  color: @bgcHeight;
}
</style>
