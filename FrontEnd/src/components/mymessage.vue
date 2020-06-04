<!-- <template>
  <el-form label-width="100px">
  <el-button type="primary" @click="showDialog2 = true">显示内容</el-button>


      <el-input v-model="act.content" type="textarea" :rows="5"></el-input>
  </el-form>
</template> -->
<template>
  <el-button type="text" @click="open">点击打开 Message Box</el-button>
</template>
<script>
import {get_receive_message} from '../api/api.js'
export default {
  data () {
    return {
      act: {
        name: '',
        tag: [],
        content: '',
        location: '',
        datetime: '',
        ddl: ''
      },
      act1:''
    }
  },
  methods: {
    open() {
      get_receive_message(
        {
          userid: this.$cookies.get('userid')

        })
      .then(response => {
        window.alert('正在接收到消息')
        this.act1 = response.data.data


      })


       this.$alert(this.act1, '你的消息', {
         confirmButtonText: '确定',
       });
    },
  
  }
}
</script>
<style>

</style>
