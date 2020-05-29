<template>
  <div>
    <el-row>
      <el-col :span="20" :offset="2">
        <h3>评论活动</h3>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="20" :offset="2">
        <el-input type="textarea" :rows="5" placeholder="请输入评论内容，不超过120字" v-model="textarea">
        </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="3" :offset="20">
        <el-button @click="addComment">发布评论</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      textarea: ''
    }
  },
  props: ['actId'],
  methods: {
    addComment () {
      console.log('addcomment')
      let _this = this
      this.$axios({
        method: 'get',
        url: '/BackEnd/comment/',
        params: {
          userid: _this.$cookies.get('userid'),
          actid: _this.actid,
          comment: _this.textarea
        }
      })
        .then(function (response) {
          window.alert('评论成功')
        })
    }
  }
}
</script>

<style>

</style>
