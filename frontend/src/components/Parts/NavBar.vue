<template>
  <div id="side-bar">
    <div class="header d-flex align-items-center justify-content-center">
        <label>{{ pageTitle }}</label>
    </div>
      <input type="checkbox" class="openSidebarMenu" id="openSidebarMenu">
      <label for="openSidebarMenu" class="sidebarIconToggle">
        <div class="spinner diagonal part-1"></div>
        <div class="spinner horizontal"></div>
        <div class="spinner diagonal part-2"></div>
      </label>
      <div id="sidebarMenu">
        <ul class="sidebarMenuInner">
          <li><router-link to="/" class="link" @click="hideSideBar">トップページ</router-link></li>
          <li><router-link to="/userList" class="link" @click="hideSideBar">ユーザー一覧</router-link></li>
          <li><router-link to="/xxxx" class="link" @click="hideSideBar">Not Found</router-link></li>
        </ul>
      </div>
      <br><br><br>
  </div>
</template>
<script>
import { ref } from 'vue'

export default {
  name: 'NavBar',
  setup() {
    // ページタイトル
    const pageTitle = ref('Title')

    // サイドバー非表示
    const hideSideBar = () => {
      document.getElementById('openSidebarMenu').checked = false
    }
    
    return {
      pageTitle,
      hideSideBar
    }
  }
}
</script>
<style scoped>
.header {
    display: block;
    margin: 0 auto;
    width: 100%;
    max-width: 100%;
    box-shadow: none;
    background-color: #FC466B;
    position: fixed;
    height: 60px!important;
    overflow: hidden;
    z-index: 10;
}
#sidebarMenu {
    height: 100%;
    position: fixed;
    left: 0;
    width: 250px;
    margin-top: 60px;
    text-align: left;
    transform: translateX(-250px);
    transition: transform 250ms ease-in-out;
    background: linear-gradient(180deg, #FC466B 0%, #3F5EFB 100%);
}
.sidebarMenuInner{
    margin:0;
    padding:0;
    border-top: 1px solid rgba(255, 255, 255, 0.10);
}
.sidebarMenuInner li{
    list-style: none;
    color: #fff;
    text-transform: uppercase;
    font-weight: bold;
    padding: 20px;
    cursor: pointer;
    border-bottom: 1px solid rgba(255, 255, 255, 0.10);
}
.sidebarMenuInner li span{
    display: block;
    font-size: 14px;
    color: rgba(255, 255, 255, 0.50);
}
.sidebarMenuInner li a{
    color: #fff;
    text-transform: uppercase;
    font-weight: bold;
    cursor: pointer;
    text-decoration: none;
}
input[type="checkbox"]:checked ~ #sidebarMenu {
    transform: translateX(0);
}

input[type=checkbox] {
    transition: all 0.3s;
    box-sizing: border-box;
    display: none;
}
.sidebarIconToggle {
    transition: all 0.3s;
    box-sizing: border-box;
    cursor: pointer;
    position: fixed;
    z-index: 99;
    height: 100%;
    width: 100%;
    top: 22px;
    left: 15px;
    height: 22px;
    width: 22px;
}
.spinner {
    transition: all 0.3s;
    box-sizing: border-box;
    position: absolute;
    height: 3px;
    width: 100%;
    background-color: #fff;
}
.horizontal {
    transition: all 0.3s;
    box-sizing: border-box;
    position: relative;
    float: left;
    margin-top: 3px;
}
.diagonal.part-1 {
    position: relative;
    transition: all 0.3s;
    box-sizing: border-box;
    float: left;
}
.diagonal.part-2 {
    transition: all 0.3s;
    box-sizing: border-box;
    position: relative;
    float: left;
    margin-top: 3px;
}
input[type=checkbox]:checked ~ .sidebarIconToggle > .horizontal {
    transition: all 0.3s;
    box-sizing: border-box;
    opacity: 0;
}
input[type=checkbox]:checked ~ .sidebarIconToggle > .diagonal.part-1 {
    transition: all 0.3s;
    box-sizing: border-box;
    transform: rotate(135deg);
    margin-top: 8px;
}
input[type=checkbox]:checked ~ .sidebarIconToggle > .diagonal.part-2 {
    transition: all 0.3s;
    box-sizing: border-box;
    transform: rotate(-135deg);
    margin-top: -9px;
}
label {
    color: #fff;
    text-transform: uppercase;
    font-weight: bold;
    text-decoration: none;
    margin-bottom: 0px;
}
.link {
    display: block;
}
</style>