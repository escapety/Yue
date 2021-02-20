<template>
  <el-container>
    <el-header><NavBar></NavBar></el-header>
    <el-main>
      <el-row>
        <el-col :span="3" :offset="1">
          <br/><br/>
          <el-button type="primary" @click="showDialog = true">创建活动</el-button>
          <el-dialog
            title="创建活动"
            :visible.sync="showDialog"
            width="70%">
            <createForm/>
          </el-dialog>
        </el-col>
        <el-col :span="18">
          <h3>所有活动</h3>
          <ActList listtype="all"/>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>
<script>
import NavBar from '@/components/NavBar'
import CreateForm from '@/components/CreateForm'
import ActList from '@/components/ActList'
export default {
  data () {
    return {
      showDialog: false
    }
  },
  components: {
    NavBar,
    CreateForm,
    ActList
  }
}
</script>
<style>
  .center{
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
