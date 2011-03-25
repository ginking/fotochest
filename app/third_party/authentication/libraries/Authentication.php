<?php
/**
* iRoam
*
* iRoam is a simple web travel application.  Meant to help you share your trips with family and friends.
*
* @package		iRoam
* @version		1.0
* @author		Derek Stegelman <stegelman.com>
* @license		Apache License v2.0
* @copyright	2010 - 2011 iRoam
*/

// ----------------------------------------------------------------

/**
* Authentiction Package
*
* @package		Authentication
* @category		Libraries
* @author		Derek Stegelman
*/

/**
 * Auth Package
 * 
 * @package Authentication
 * @version 1.0
 * @author Derek Stegelman
 * @copyright 2011 Derek Stegelman
 * @link http://stegelman.com
 */


// ------------------------------------------------------------------------

/**
 * Authencation
 * 
 * @package Authentication
 * @author Derek Stegelman
 * 
 * Dependencies
 *  - CI 2.0 with package support
 *  - Derek Stegelman's Core Model
 * 
 */



class Authentication {
    
    /**
     *
     * @var object   CI Super object
     */
    private $_ci;
    
    /**
     * 
     * Constructor - Grab and load dependencies.
     * 
     */
    
    public function __construct() {
    	log_message('info', 'Trying to load auth lib');
        $this->_ci =& get_instance();
        log_message('info', 'got ci Instance');
        $this->_ci->load->model('Authentication_mdl');
        log_message('info', 'model loaded');
        $this->_ci->load->config('auth');
        
        log_message('info', 'config loaded');
        $this->_ci->load->library('session');
        log_message('info', 'Auth lib loaded');
    }
    
    /**
    * function _generate_salt()
    *
    */
    
    private function _generate_salt()
    {
        $this->_ci->load->helper('string');
        return sha1(random_string('alnum', 32));
    }
    
    /*
       * @var $identity_field  and $password
     * @author Derek Stegelman
     * @returns user_id or -1 if failed int
     *
     * @var $identity_field  and $password
     * @author Derek Stegelman
     * @returns user_id or -1 if failed int
     */
    
    public function log_in($identity, $password)
    {
        //Check for user for username first
        log_message('info', 'get where for username');
	$user_object = $this->_ci->Authentication_mdl->get_where('username', $identity);
        
        if ($user_object->num_rows() !==1)
        {
            // Check for the email now.
            log_message('debug', 'Username was not found');
            $user_object = $this->_ci->Authentication_mdl->get_where('email', $identity);
            if ($user_object->num_rows() !==1)
            {
                //Okay now we really couldn't find the user.  Bastard.
                log_message('info', 'User ' . $identity . ' was not found.');
                return -1;
            }
            
        }

	if (sha1($password.$user_object->row('salt')) == $user_object->row('password'))
	{
		$data = array(
			'user_id'   => $user_object->row('id'),
			'username'  => $user_object->row('username'),
			'email'     => $user_object->row('email'),
			'salt'      => $user_object->row('salt'),
		);
		
		$this->_ci->session->set_userdata($data);
		
		return $user_object->row('id');
	}
        log_message('info', 'User ' . $identity . ' could not be authenticated.');
	return -1;
    }
    
    /**
     * Register
     * 
     * @author Derek Stegelman
     * 
     * @param string $username
     * @param string $email
     * @param string $password
     * @param string $first_name
     * @param string $last_name 
     */
    
    public function register($username, $email, $password, $first_name, $last_name)
    {
    	log_message('info', 'HEY, you reached the auth register method');
        if ($this->_ci->Authentication_mdl->exist('username', $username) OR $this->_ci->Authentication_mdl->exist('email', $email))
        {
        	log_message('info', 'Username exists');
            return FALSE;
        }
        
        $user_salt = $this->_generate_salt();
        log_message('info', 'Salt generated');
        
        
        $user_data = array('username'=>$username, 'email'=>$email, 'salt'=>$user_salt, 'password'=>sha1($password.$user_salt),
                           'first_name'=>$first_name, 'last_name'=>$last_name);
        
        //Create user 
        log_message('info', 'Executing create method');
        return $this->_ci->Authentication_mdl->create($user_data);
        
    }
    
    public function log_out()
    {
        $this->_ci->session->sess_destroy();
    }

    public function get_user($user_id)
    {
        return $this->_ci->Authentication_mdl->get($user_id);
    }
    

}