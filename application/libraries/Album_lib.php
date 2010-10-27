<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Album_lib
 *
 * @author derek
 */
class Album_lib {

    private $ci;

    var $albumName;
    var $albumCreateDate;
    var $albumID;
    var $albumParentID;
    var $albumDesc;
    var $albumFriendlyName;
    

    public function __contruct()
    {
        $this->ci = get_instance();
    }


    /**********************************************
     *  createAlbum
     *
     *  Params(); None - Accepts object properties
     *  returns null; 
     * ********************************************
     */

    public function createAlbum(){

        log_message('info', 'Executing createAlbum method'); // Log for information purposes.
        // Once a new photo is uploaded to the album it bcomes the thumbnail....

        // Load the Model

        $this->ci->load->model('Album_mdl');

        // Load up the variables
        $this->ci->Album_mdl->albumName = $this->albumName;
        $this->ci->Album_mdl->albumParentID = $this->albumParentID;
        $this->ci->Album_mdl->albumFriendlyName = $this->albumFriendlyName;

        // Call the CRUD Method
        $this->ci->Album_mdl->create();

        mkdir("./img_stor/albums/" . $this->albumName);
        mkdir("./img_stor/albums/" . $this->albumName . "/originals");
        mkdir("./img_stor/albums/" . $this->albumName . "/thumbs");
    }
    
    /**
     *  Delete Album
     * @param AlbumID, and the path of the site.  (Can we grab this here???)
     * 
     * 
     */



    public function deleteAlbum($albumID, $path){

        // Load the Album Model
        $this->ci->load->model('Album_mdl');

        // Call the delete Method
        $this->ci->Album_mdl->delete($albumID);
        

        $deletePhotos = "DELETE FROM $this->photoTable WHERE photoAlbumID = $albumID";
        log_message('info', 'album_mdl::deleteAlbum executed a query ' . $deletePhotos);
        $this->db->query($deletePhotos);

        $this->load->helper('file');

        delete_files($path . "img_stor/albums/" . $this->albumName);
        rmdir('./img_stor/albums/' . $this->albumName);
        log_message('info', 'Removing directory for album ' . $this->albumName);

    }



    public function findAlbumThumbnails($albumID, $neededPhotos= 3){

        // First check to see if the album has some thumbs allready/needs to have pictures in it to do this.

        $grabbedPhotos = 0;
        $currentAlbum = $albumID;
        $inNeed = $neededPhotos;
        $this->ci->load->model('Album_mdl');

        $albumThumbs = $this->ci->Album_mdl->getAlbumCount($albumID);


        if ($albumThumbs >= $neededPhotos)
        {
            // Good..

            $imgs = $this->ci->Album_mdl->getAlbumThumbnails($albumID, $neededPhotos);


            return $imgs;
        }
        else
        {

            // Begin finding other phtoos.
            while($grabbedPhotos < $neededPhotos)
            {

                $childPhotos = $this->ci->Album_mdl->getAlbumThumbnails($currentAlbum, $neededPhotos);

                if($childPhotos->num_rows() >= $neededPhotos)
                {

                    $grabbedPhotos = $childPhotos->num_rows();
                    return $childPhotos;
                    break;

                }
                else
                {

                    $currentAlbum = $this->ci->Album_mdl->findChildID($currentAlbum);

                    $grabbedPhotos = 0 ;

                    if($currentAlbum == 0)
                    {

                        // This shouldn't happen....
                        return $this->ci->Album_mdl->getAlbumThumbnails($currentAlbum);
                        break;
                    }
                }
            }
        }


    }

//    public function getAlbumFriendlyName($albumID){
//
//        //Deprecated...
//        log_message('error', 'getAlbumFriendlyName has been used.  This method is deprecated...');
//        $selectAlbum = "SELECT * FROM $this->albumTable WHERE albumID = $albumID";
//        log_message('info', 'Album_mdl::getAlbumFriendlyName() is executing a query ' . $selectAlbum);
//        $exe = $this->db->query($selectAlbum);
//        foreach($exe->result() as $row){
//            $albumFriendly = $row->albumFriendlyName;
//        }
//        return $albumFriendly;
//    }
//
//    public function getAlbumName($albumID){
//        $selectAlbum = "SELECT * FROM $this->albumTable WHERE albumID = $albumID";
//        log_message('info', 'Album_mdl::getAlbumName is executing a query ' . $selectAlbum);
//        $execute = $this->db->query($selectAlbum);
//        foreach($execute->result() as $row){
//            $albumName = $row->albumName;
//        }
//        return $albumName;
//    }
}
?>