<template>
  <el-card>
    <div slot="header">
      <span>我的资料</span>
      <el-button style="float: right; padding: 3px 0" type="text">修改</el-button>
    </div>
    <div>
      <img src="../assets/head.png" height="100" width="100"/>
      <el-form label-position='left' label-width="50px">
        <el-form-item label='姓名'>{{name}}</el-form-item>
        <el-form-item label='性别'>{{gender}}</el-form-item>
        <el-form-item label='级别'>{{level}}</el-form-item>
        <el-form-item label='学院'>{{school}}</el-form-item>
      </el-form>
    </div>
  </el-card>
</template>
<script>
export default {
  data () {
    return {
      name: '李华',
      gender: '男',
      level: '16级',
      school: '信科',
    }
  }
}
</script>
<style>

</style>
