<?php
$this->load->view('admin/header');
$data['pageNum'] = 2;
$this->load->view('admin/navigation', $data);
?>

    <div class="content right" id="viewSingleAlbum">
        <h2><?php echo $albumFriendlyName; ?></h2>
       <?php if($photos->num_rows() == 0) { ?>
        <h3>This album has no photos.  Do you want to <?php echo anchor('admin/photoUpload/' . $albumID, 'add some?'); ?></h3>
        <?php } ?>
       <?php foreach($photos->result() as $row) { ?>
        <div class="photo">
            <a href="<?php echo base_url(); ?>img_stor/albums/<?php echo $row->albumName; ?>/thumbs/<?php echo $row->photoFileName; ?>" class="preview" title="<?php echo $row->photoDesc; ?>">
            <img src="<?php echo base_url(); ?>img_stor/albums/<?php echo $row->albumName; ?>/thumbs/<?php echo $row->photoFileName; ?>" width="75">
            </a>
            <h3><?php echo $row->photoTitle; ?></h3>
            <p>
                <?php echo $row->photoDesc; ?>
            </p>
            <dl>

                <dt>Album</dt>
                <dd><?php echo $row->albumFriendlyName; ?></dd>


            </dl>
            <ul class="actions">
                <li><a href="<?php echo base_url(); ?>admin/editPhoto/<?php echo $row->photoID; ?>/N" class="button" rel="facebox"><span>Edit</span></a></li>
                <li><a href="<?php echo base_url(); ?>admin/movePhoto/<?php echo $row->photoID; ?>" class="button" rel="facebox"><span>Move</span></a></li>
                <li><a href="<?php echo base_url(); ?>admin/deletePhoto/<?php echo $row->photoID; ?>" class="button" rel="facebox"><span>Delete</span></a></li>
            </ul>
        </div>
        <?php } ?>


        <div class="pagination">
            <?php echo $pages; ?>
        </div>
    </div>
    <?php $data['showAlbum'] = FALSE; ?>
<?php $data['showUserButton'] = TRUE; ?>
    <?php $this->load->view('admin/sidebar', $data); ?>
    <?php $this->load->view('admin/footer'); ?>
