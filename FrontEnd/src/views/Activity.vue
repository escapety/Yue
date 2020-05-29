<template>
  <el-container>
    <el-header><NavBar></NavBar></el-header>
    <el-body>
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
          <el-button v-if="inAct" plain disabled>你已加入活动</el-button>
          <el-button v-else type='primary' @click="joinAct">加入活动</el-button>
        </el-col>
      </el-row>
      <!-- <CommentArea :actId='actInfo.id'/> -->
    </el-body>
  </el-container>
</template>
<script>
import NavBar from '@/components/NavBar'
import CommentArea from '@/components/CommentArea'
export default {
  data () {
    return {
      actInfo: {
        name: 'name',
        id: '',
        theme: 'theme',
        intr: 'intr',
        attr: 'attr',
        location: 'location',
        time: 'time',
        deadline: 'deadline'
      },
      inAct: false
    }
  },
  created: function () {
    this.actInfo.id = this.$route.query.id
    this.getAct(this.actInfo.id)
  },
  methods: {
    getAct (actid) {
      let _this = this
      this.$axios({
        method: 'get',
        url: '/BackEnd/get_activity/',
        params: {
          id: actid
        }
      })
        .then(function (response) {
          console.log(response.data)
          let act = response.data
          _this.actInfo.name = act.name
          _this.actInfo.theme = act.theme
          _this.actInfo.intr = act.intr
          _this.actInfo.attr = act.attr
          _this.actInfo.location = act.location
          _this.actInfo.time = act.time
          _this.actInfo.deadline = act.deadline
        })
    },
    joinAct () {
      let _this = this
      this.$axios({
        method: 'get',
        url: '/BackEnd/join_activity/',
        params: {
          userid: this.$cookies.get('userid'),
          actid: _this.actInfo.id
        }
      }).then(function (response) {
        console.log(response)
        _this.inAct = true
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
