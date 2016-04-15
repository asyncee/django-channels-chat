$(function(){
    function log(msg) {
        console.log('new message', msg)
        var $log = $('#log');
        $log.append($('<div/>').addClass(msg.type).text(msg.user + ': ' + msg.text))
    }

    $('#connect').on('click', function(){
        socket = new WebSocket("ws://127.0.0.1:9000/chat/");
        socket.onmessage = function(e) {
            log(JSON.parse(e.data));
        }
        socket.onopen = function() {
            socket.send(JSON.stringify({
                type: 'connect',
                username: $('#username').val()
            }))
        }
    })

    $('#text-input').on('keypress', function(e) {
        if (e.which == 13) {
            socket.send(
                JSON.stringify({
                    type: 'message',
                    text: $('#text-input').val()
                })
            );
            $('#text-input').val('');
        }
    })
})
