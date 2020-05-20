<template>
  <el-form label-width="100px">
    <el-form-item label="活动名称">
      <el-input v-model="act.name"></el-input>
    </el-form-item>
    <el-form-item label="活动主题">
      <el-input v-model="act.theme"></el-input>
    </el-form-item>
    <el-form-item label="活动类别">
      <el-radio-group v-model="act.type">
        <el-radio :label="1">运动</el-radio>
        <el-radio :label="2">学术</el-radio>
        <el-radio :label="3">娱乐</el-radio>
        <el-radio :label="4">吃喝</el-radio>
        <el-radio :label="5">其他</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="活动属性">
      <el-input v-model="act.attr"></el-input>
    </el-form-item>
    <el-form-item label="活动地点">
      <el-input v-model="act.location"></el-input>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-date-picker v-model="act.datetime" type="datetime"></el-date-picker>
    </el-form-item>
    <el-form-item label="报名截止时间">
      <el-date-picker v-model="act.deadline" type="datetime"></el-date-picker>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="create('act')">确认</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
export default {
  data () {
    return {
      act: {
        name: '',
        theme: '',
        type: '',
        attr: '',
        location: '',
        datetime: '',
        deadline: ''
      }
    }
  },
  methods: {
    create (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log('successful created')
        } else {
          console.log('failed to create')
        }
      })
    }
  }
}
</script>
<style>

</style>
