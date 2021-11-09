import React, { useState } from 'react';
import styles from './styles';

import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/material/Menu';
import Icon from '@mui/material/Icon';

import { Link } from 'react-router-dom';

const Header = () => { 
  return ( 
    <div className={styles.root}>
    <AppBar position="static" elevation={0}>
        <Toolbar variant="dense">
            <Link to="/" style={styles.appLink}>
                <Typography style={styles.appTitle} >
                    Garble: Audio Summarizer
                </Typography>
            </Link>

            <div style={styles.grow} />


            <div>
                <IconButton color="inherit" component={Link} to="/">
                    <Icon>home</Icon>
                    <Typography variant="caption">&nbsp;Home</Typography>
                </IconButton>
                <IconButton color="inherit" component={Link} to="/currentmodel">
                    <Icon>model_training</Icon>
                    <Typography variant="caption">&nbsp;Model</Typography>
                </IconButton>
            </div>
        </Toolbar>
    </AppBar>
</div>
  )
}; 

export default Header;
