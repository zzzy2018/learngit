/**
 * Created by tarena on 18-10-22.
 */
$(function(){
  //表示手机号是否已经被注册过的状态值
  // var registStatus = 1;
  window.registStatus = 1;

  /**1.为uhpone控件绑定blur事件*/
  $("input[name='uphone']").blur(function(){
    //如果文本框内没有任何东西则返回
    if($(this).val().trim().length == 0)
      return;
    //如果文本框内有数据的话则发送ajax请求判断数据是否存在
    $.get(
      '/check_uphone/',
      {'uphone':$(this).val()},
      function(data){
        $("#uphone-tip").html(data.msg);
        //为registStatus赋值，以便在提交表单时使用
        window.registStatus = data.status;
        console.log("data.status:"+data.status);
      },'json'
    );
  });
  /**2.为#formReg表单元素绑定submit事件*/
  $("#formReg").submit(function(){
    //判断registStatus的值，决定表单是否要被提交
    console.log('registStatus:'+registStatus);
    if(window.registStatus == 1)
      return false;
    return true;
  });
});