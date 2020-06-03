<template>
  <div style="height:40px;">
  <el-menu 
    mode="horizontal"
    background-color="#545c64"
    active-text-color="#ffd04b"
    text-color="#fff"
    router>
    <el-menu-item index="main">所有活动</el-menu-item>
    <el-submenu index="2">
      <template slot="title">我的</template>
      <el-menu-item index="/profile">我的资料</el-menu-item>
      <el-menu-item index="/">注销</el-menu-item>
    </el-submenu>
  </el-menu>
  </div>
</template>

<script>
export default {
  methods: {
  }
}
</script>
<style scoped>
</style>
