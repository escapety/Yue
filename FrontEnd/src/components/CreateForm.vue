<template>
  <el-form label-width="100px" ref="create">
    <el-form-item label="活动名称" prop="name">
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
    <el-form-item label="活动内容">
      <el-input v-model="act.intr"></el-input>
    </el-form-item>
    <el-form-item label="活动属性">
      <el-input v-model="act.attr"></el-input>
    </el-form-item>
    <el-form-item label="活动地点">
      <el-input v-model="act.location"></el-input>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-date-picker v-model="act.time" type="datetime"></el-date-picker>
    </el-form-item>
    <el-form-item label="报名截止时间">
      <el-date-picker v-model="act.deadline" type="datetime"></el-date-picker>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="create">确认</el-button>
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
        time: '',
        deadline: '',
        intr: ''
      }
    }
  },
  methods: {
    create () {
      let _this = this
      this.$axios({
        method: 'get',
        url: '/BackEnd/new_activity/',
        params: {
          name: _this.act.name,
          theme: _this.act.theme,
          location: _this.act.location,
          time: _this.act.time,
          deadline: _this.act.deadline,
          sponsor: _this.$cookies.get('userid'),
          intr: _this.act.intr,
          type: _this.act.type,
          attr: _this.act.attr
        }
      })
        .then(function (response) {
          window.alert('活动创建成功')
        })
    }
  }
}
</script>
<style>

</style>
