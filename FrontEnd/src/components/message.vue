<template>
  <el-form label-width="100px">
    <el-form-item label="收件人">
      <el-input v-model="act.name"></el-input>
    </el-form-item>

    <el-form-item label="发件时间">
      <el-date-picker v-model="act.time" type="datetime"></el-date-picker>
    </el-form-item>

    <el-form-item label="内容">
      <el-input v-model="act.content" type="textarea" :rows="5"></el-input>
    </el-form-item>


    <el-form-item>
      <el-button type="primary" @click="onSubmit">发送</el-button>
    </el-form-item>
    <!-- <el-form-item>
      <el-button type="primary" @click="create('act')">确认</el-button>
    </el-form-item> -->
  </el-form>
</template>
<script>
import {send_message} from '../api/api.js'
export default {
  data () {
    return {
      act: {
        name: '',
        tag: [],
        time:'',
        content: '',
        location: '',
        datetime: '',
        ddl: ''
      }
    }
  },
  methods: {
    onSubmit () {
      send_message({
        // name: this.act.name,
        // content: this.act.content,
        // sponsor: this.$cookies.get('userid'),
        userid : this.$cookies.get('userid'),
        targetid : this.act.name,
        text:this.act.content,
        time:this.act.time,
        // name: this.act.name,
        // theme: this.act.theme,
        // location: this.act.location,
        // time: this.act.time,
        // deadline: this.act.deadline,
        // sponsor: this.$cookies.get('userid'),
        // intr: this.act.intr,
        // type: this.act.type,
        // attr: this.act.attr
      })
        .then(response => {
          window.alert('消息已经发送')


        })
    }
  }
}
</script>
<style>

</style>
