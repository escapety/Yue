<template>
  <div>
    <el-header><NavBar></NavBar></el-header>
    <el-body>
      <p/>
      <el-page-header @back="goBack" content="活动详情"></el-page-header>
      <el-row>
        <el-col :span="8" :offset="4">
          <h3>{{actInfo.name}}</h3>
        </el-col>
        <el-col :span="8">
          <p>id：{{actInfo.id}}</p>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="16" :offset="4">
          <p>主题：{{actInfo.theme}}</p>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="16" :offset="4">
          <p>内容：{{actInfo.theme}}</p>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8" :offset="4">
          <p>属性：{{actInfo.attr}}</p>
        </el-col>
        <el-col :span="8">
          <p>地点：{{actInfo.location}}</p>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="8" :offset="4">
          <p>活动时间：{{actInfo.time}}</p>
        </el-col>
        <el-col :span="8">
          <p>报名截止时间：{{actInfo.deadline}}</p>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="4" :offset="10">
          <el-button v-show="inAct" plain disabled>你已加入活动</el-button>
          <el-button v-show="!inAct" type='primary' @click="joinAct">加入活动</el-button>
        </el-col>
      </el-row>
      <CommentArea actId='actInfo.id'/>
    </el-body>
  </div>
</template>
<script>
import NavBar from '@/components/NavBar'
import CommentArea from '@/components/CommentArea'
import {join_activity} from '../api/api.js'
export default {
  data () {
    return {
      actInfo: {},
      inAct: false
    }
  },
  mounted: function () {
    this.actInfo = this.$route.params.act
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    },
    joinAct () {
      join_activity({
        userid: this.$cookies.get('userid'),
        actid: this.actInfo.id
      }).then(function (response) {
        console.log(response)
        this.inAct = true
      })
    }
  },
  components: {
    NavBar,
    CommentArea
  }
}
</script>
<style>

</style>
