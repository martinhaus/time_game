
$("#rfidSubmit").on("submit", function(){
    return false;
})

$('#rfidId').keydown(function (e){
    if(e.keyCode == 13){
        let tagId = $('#rfidId').val();
        getPlayer(tagId);
    }
})

function loadPlayerValues(player) {
    $('#rfidId').val("");
    $('#tagId').val(player.rfid_id);
    $('#timeLeft').val(player.time);
}

function getPlayer(rfidId) {
    $.get( "/api/get/" + rfidId, function (data) {
        loadPlayerValues(data);
    });
}

function getAllPlayers() {
    $.get("/api/get_all", function( data ) {
        return data;
    });
}

$('#updatePlayer').on("click", function () {
    let tagId = $('#tagId').val();
    let time = $('#timeLeft').val();
    $.post("/api/update", {rfid_id: tagId, time: time}, function (response) {
        console.log('done');
    })
});

function addPlayer(rfidId, time) {

}