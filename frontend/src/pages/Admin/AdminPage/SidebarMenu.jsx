import React from "react";
import Divider from '@mui/material/Divider';
import { Link as RouterLink } from 'react-router';
import { Link } from '@mui/material';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MailIcon from '@mui/icons-material/Mail';
import Toolbar from '@mui/material/Toolbar';

const SidebarMenu = () => {
    return (
        <>
            <Toolbar />
                  <Divider />
                  <List>
                    <ListItem key="dashboard" disablePadding>
                        <ListItemButton>
                          <ListItemIcon>
                            <InboxIcon />
                          </ListItemIcon>
                          <Link
                            to="/admin/dashboard" 
                            component={RouterLink}
                            underline="none"
                            color="inherit"
                            >Dashboard
                            </Link>
                        </ListItemButton>
                    </ListItem>
            
                    <ListItem key="speakers" disablePadding>
                        <ListItemButton>
                          <ListItemIcon>
                            <InboxIcon />
                          </ListItemIcon>
                          <Link
                            to="/admin/speakers" 
                            component={RouterLink}
                            underline="none"
                            color="inherit"
                            >Speakers
                            </Link>
                        </ListItemButton>
                    </ListItem>
            
                  </List>
                  <Divider />
                  <List>
                    {['All mail', 'Trash', 'Spam'].map((text, index) => (
                      <ListItem key={text} disablePadding>
                        <ListItemButton>
                          <ListItemIcon>
                            {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
                          </ListItemIcon>
                          <ListItemText primary={text} />
                        </ListItemButton>
                      </ListItem>
                    ))}
                  </List>
        </>
    );
}

export default SidebarMenu;