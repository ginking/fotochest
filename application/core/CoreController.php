<?php

class CoreController extends CI_Controller {
	
	public function __construct()
	{
            parent::__construct();
            // Enable profiler in debug mode.
            if($this->config->item('environment') == 'dev' OR $this->config->item('environment') == 'staging')
            {
                $this->output->enable_profiler(TRUE);
            }
	}

        public function  __destruct()
        {
            log_message('info', 'last query ' . $this->db->last_query());
        }
	
	
}

?>