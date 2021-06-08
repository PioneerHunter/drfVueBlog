import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// 在原型上自定义appendIfExists方法，全局可用
URLSearchParams.prototype.appendIfExists = function (key, value) {
  if (value !== null && value !== undefined) {
    this.append(key, value);
  }
};

createApp(App).use(store).use(router).mount("#app");
