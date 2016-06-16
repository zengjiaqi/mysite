$('#login-button').click(function()
{
    var user = $('#user').val();
    var password = $('#password').val();
    if (user === "" || password === "")
    {
        alert("用户名或密码不能为空！");
    }
    else {
        $.ajax({
            type: "POST",
            dataType:'json',
            async: false,
            url: "loginapi",
            data: {
                "user":user,
                "password":password,
            },
            success: function(data){
                if (data["result"]===1)
                {
                    window.location.href="http://127.0.0.1:8000/manager/index/";
                    // alert(data['result'])
                }
                else
                {
                    alert(data['msg']);
                }

            }
        });
    } 
});
