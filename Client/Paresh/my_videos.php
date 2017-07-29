<?php session_start();
if($_SESSION['user_id']=='')
    header("location: index.php");
$mysqli = mysqli_connect("localhost","root","","Ceque");
if(!$mysqli)
    die ("Could not connect to database");
$user_name = $mysqli->query("SELECT email FROM users WHERE id = ".$_SESSION['user_id'].";")->fetch_assoc()['email'];
?>
<html><head><title> Videos</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <?php
    $video_error = '';
    if($_SERVER['REQUEST_METHOD']=="POST")
    {
        if(isset($_POST['comment_submit']))
        {
            $comment = filter_var(trim(htmlspecialchars($mysqli->real_escape_string($_POST['comment_text'])),FILTER_SANITIZE_STRING));
            $mysqli->query("INSERT INTO comments (video_id,commentor_id,comment) VALUES(".$_POST['video_id_to_work'].",".$_SESSION['user_id'].",'$comment')");
            header("Refresh:0");
        }
        else if(isset($_POST['delete']))
        {
            $mysqli->query("DELETE FROM videos WHERE video_id=".$_POST['video_id_to_work'].";");
            header("Refresh:0");
        }
        else
            if(isset($_FILES['video']))
                if(stristr($_FILES['video']['type'],"video"))
                    $mysqli->query("INSERT INTO videos (id,video_name) VALUES (".$_SESSION['user_id'].",'".$_FILES['video']['name']."');");
                else $video_error="It is not a video";
            else $status = "Please enter a video";
    }
    ?>
</head>
<body>
<div class="container text-center">
    <div class="row">
        <div class="col-xs-3">
            <h3>Upload new video</h3>
        </div>
        <div class="col-xs-9" style="margin-top: 20px;">
            <form class="form-inline" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <input type="file" name="video">
                </div>
                <button class="btn btn-primary">Upload</button>
            </form>
        </div>
    </div>
    <hr>
        <?php
        $result = $mysqli->query("SELECT * FROM videos WHERE id=".$_SESSION['user_id']." ORDER BY video_id DESC");
        if($result->num_rows>0)
            while($row = $result->fetch_assoc())
        {
            echo "<h1>".$row['video_name']." uploaded by user ".$mysqli->query("SELECT email FROM users WHERE id = ".$row['id'].";")->fetch_assoc()['email'].'</h1><br><br>
<form method="post">
<textarea class="form-control" rows="2" cols="30" placeholder="Comment here" name="comment_text"></textarea>
<input type="hidden" name="video_id_to_work" value="'.$row['video_id'].'">
<input type="submit" class="btn btn-primary" name="comment_submit" value="Comment">
<input type="submit" class="btn btn-default" name="delete" value="Delete Video">
</form>';
            $comments_table = $mysqli->query("SELECT * FROM comments WHERE video_id=".$row['video_id']." ORDER BY comment_id DESC");
            if($comments_table->num_rows>0)
                while($comment_row = $comments_table->fetch_assoc())
                    echo "<h3>".$mysqli->query("SELECT email FROM users WHERE id = ".$comment_row['commentor_id'].";")->fetch_assoc()['email']." says : ".$comment_row['comment']."</h3>";
        }
        ?>
</div>
</body>
</html>