<template>
  <blog-header></blog-header>

  <div id="grid">
    <div id="signup">
      <h3>注册账号</h3>
      <form action="">
        <div class="form-ele">
          <span>账号：</span>
          <input type="text" placeholder="输入用户名" v-model="signupName" />
        </div>
        <div class="form-ele">
          <span>密码：</span>
          <input type="password" placeholder="输入密码" v-model="signupPwd" />
          {{ signupPwd }}
        </div>
        <div class="form-ele">
          <button @click.prevent="signup">提交</button>
        </div>
      </form>
    </div>

    <div id="signin">
      <h3>登录账号</h3>
      <form action="">
        <div class="form-ele">
          <span>账号：</span>
          <input type="text" placeholder="输入用户名" v-model="signinName" />
        </div>

        <div class="form-ele">
          <span>密码：</span>
          <input type="password" placeholder="输入密码" v-model="signinPwd" />
        </div>

        <div class="form-ele">
          <button @click.prevent="signin">提交</button>
        </div>
      </form>
    </div>
  </div>

  <blog-footer></blog-footer>
</template>

<script>
import axios from "axios";
import BlogHeader from "@/components/BlogHeader.vue";
import BlogFooter from "@/components/BlogFooter.vue";

export default {
  name: "Login",
  components: {
    BlogHeader,
    BlogFooter,
  },
  data: function () {
    return {
      signupName: "",
      signupPwd: "",
      signinName: "",
      signinPwd: "",
      signupResponse: null,
    };
  },
  methods: {
    // 注册
    signup() {
      const that = this;
      axios
        .post("/api/user/", {
          username: String(that.signupName),
          password: String(that.signupPwd),
        })
        .then(function (response) {
          that.signupResponse = response.data;
          alert("注册成功！快去登录吧！");
        })
        .catch(function (error) {
          alert("注册失败，请重试");
          console.log(error);
        });
    },
    // 登录
    signin() {
      const that = this;
      axios
        .post("/api/token/", {
          username: String(that.signinName),
          password: String(that.signinPwd),
        })
        .then(function (response) {
          const storage = localStorage;
          const expiredTime = Date.parse(response.headers.date) + 60000;

          // 本地缓存
          storage.setItem("access.myblog", response.data.access);
          storage.setItem("refresh.myblog", response.data.refresh);
          storage.setItem("expiredTime.myblog", expiredTime);
          storage.setItem("username.myblog", that.signinName);

          axios
            .get("/api/user/" + that.signinName + "/")
            .then(function (response) {
              storage.setItem("isSuperuser.myblog", response.data.is_superuser);
              // 登录成功后跳转到首页
              that.$router.push({ name: "Home" });
              alert("欢迎" + that.signinName);
            });
        })
        .catch((error) => {
          alert("登录失败，请重试");
          console.log(error);
        });
    },
  },
};
</script>

<style lang="less" scoped>
#grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
// 注册
#signup {
  text-align: center;
}
.form-ele {
  padding: 10px;
}
input {
  height: 25px;
  padding-left: 10px;
}
button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: gray;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
// 登录
#signin {
  text-align: center;
}
</style>
