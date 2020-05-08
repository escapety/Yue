<template>
  <el-container>
    <el-header><NavBar></NavBar></el-header>
    <el-body>
      <el-row>
        <el-col :span="5" :offset='1'>
          <br/><br/>
          <profileCard/>
        </el-col>
        <el-col :span="17" :offset='1'>
          <h3>我创建的活动</h3>
          <ActList listtype="created"/>
          <h3>我参加的活动</h3>
          <ActList listtype="joined"/>
        </el-col>
      </el-row>
    </el-body>
  </el-container>
</template>
<script>
import ActList from '@/components/ActList'
import NavBar from '@/components/NavBar'
import profileCard from '@/components/profileCard'
export default {
  components: {
    ActList,
    NavBar,
    profileCard
  }
}
</script>
<style>

</style>
