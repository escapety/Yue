<template>
  <el-row>
    <el-col :span="2">
      <img src="../assets/logo.png" height="75" width="75"/>
    </el-col>
    <el-col :span="20">
      <el-menu mode="horizontal" @select="handleSelect" router>
      <el-submenu index="1">
        <template slot="title">所有活动</template>
        <el-menu-item index="main">娱乐类</el-menu-item>
        <el-menu-item index="main">学术类</el-menu-item>
        <el-menu-item index="main">运动类</el-menu-item>
        <el-menu-item index="main">吃喝类</el-menu-item>
      </el-submenu>
      <el-submenu>
        <template slot="title">我的</template>
        <el-menu-item index="profile">我的资料</el-menu-item>
        <el-menu-item index="/">注销</el-menu-item>
      </el-submenu>
    </el-menu>
    </el-col>
  </el-row>
</template>

<script>
export default {
  methods: {
    handleSelect: function () {

    }
  }
}
</script>
<style>

</style>
