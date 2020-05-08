<template>
  <el-form label-width="100px">
    <el-form-item label="活动主题">
      <el-input v-model="act.theme"></el-input>
    </el-form-item>
    <el-form-item label="活动标签">
      <el-checkbox-group v-model="act.tag">
        <el-checkbox label="标签一"></el-checkbox>
        <el-checkbox label="标签二"></el-checkbox>
        <el-checkbox label="标签三"></el-checkbox>
        <el-checkbox label="标签四"></el-checkbox>
        <el-checkbox label="标签五"></el-checkbox>
      </el-checkbox-group>
    </el-form-item>
    <el-form-item label="活动内容">
      <el-input v-model="act.content" type="textarea" :rows="3"></el-input>
    </el-form-item>
    <el-form-item label="活动地点">
      <el-input v-model="act.location"></el-input>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-date-picker v-model="act.datetime" type="datetime"></el-date-picker>
    </el-form-item>
    <el-form-item label="报名截止时间">
      <el-date-picker v-model="act.ddl" type="datetime"></el-date-picker>
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
        theme: '',
        tag: [],
        content: '',
        location: '',
        datetime: '',
        ddl: ''
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
