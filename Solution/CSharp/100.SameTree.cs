static public bool IsSameTree(TreeNode root1, TreeNode root2) {
	if (root1 == null &amp;&amp; root2 == null) {
		return true;
	}
	if ((root1 == null &amp;&amp; root2 != null) || (root1 != null &amp;&amp; root2 == null)) {
		return false;
	}
	if (root1.val != root2.val) {//=C5=D0=B6=CF=C3=BF=B8=F6=BD=DA=B5=E3=B5=C4=D6=B5=CA=C7=B7=F1=CF=E0=B5=C8=A3=AC=C8=E7=B9=FB=C8=A5=B3=FD=B4=CB=C5=D0=B6=CF=A3=AC=D4=F2=C5=D0=B6=CF=C1=BD=B8=F6=B6=FE=B2=E6=CA=F7=CA=C7=B7=F1=BD=E1=B9=B9=CF=E0=B5=C8
		return false;
	}
	return IsSameTree(root1.left, root2.left) &amp;&amp; IsSameTree(root1.right, root2.right);
}
bool  BTreeCompare=A3=A8BTreeNode_t *pRoot1, BTreeNode_t *pRoot2)  
{  
    if( pRoot1 == NULL &amp;&amp; pRoot2 == NULL )  
        return false;  
  
  
    queue <BTreeNode_t *> que1;  
    queue <BTreeNode_t *> que2;  
  
  
    que1.push(pRoot1);  
    que2.push(pRoot2);  
  
  
    int curLevelNodeTotal1 = 0;  
    int curLevelNodeTotal2 = 0;  
  
  
    bool flag = true; //=D7=F7=CE=AA=B1=C8=BD=CF=B2=BB=D2=BB=D6=C2=CA=B1=CC=F8=B3=F6=B1=EA=CA=B6  
    while( ( !que1.empty()) &amp;&amp; ( !que2.empty())) //=B5=B1=C1=BD=B8=F6=B6=D3=C1=D0=BE=F9=B2=BB=CE=AA=BF=D5=CA=B1=A3=AC=B2=C5=BD=F8=D0=D0=B1=C8=BD=CF  
    {  
        curLevelNodeTotal1 = que1.size();  //=BB=F1=C8=A1=CA=F71=B5=C4=B5=B1=C7=B0=B2=E3=BD=DA=B5=E3=D7=DC=CA=FD  
        curLevelNodeTotal2 = que2.size(); //=BB=F1=C8=A1=CA=F72=B5=C4=B5=B1=C7=B0=B2=E3=BD=DA=B5=E3=D7=DC=CA=FD  
        if( curLevelNodeTotal1 != curLevelNodeTotal2){  
            flag = false;//=B5=B1=C7=B0=B2=E3=BD=DA=B5=E3=D7=DC=CA=FD=B6=BC=B2=BB=D2=BB=D6=C2=A3=AC=B2=BB=D0=E8=D2=AA=B1=C8=BD=CF=C1=CB=A3=AC=D6=B1=BD=D3=CC=F8=B3=F6  
            break;  
        }  
        int cnt1 = 0;//=B1=E9=C0=FA=B1=BE=B2=E3=BD=DA=B5=E3=CA=B1=B5=C4=BC=C6=CA=FD=C6=F7  
        int cnt2 = 0;  
        while( cnt1 < curLevelNodeTotal1  &amp;&amp; cnt2 < curLevelNodeTotal2){  
            ++cnt1;  
            ++cnt2;  
            pRoot1 = que1.front();  
            que1.pop();  
            pRoot2 = que2.front();  
            que2.pop();  
  
            //=B1=C8=BD=CF=B5=B1=C7=B0=BD=DA=B5=E3=D6=D0=CA=FD=BE=DD=CA=C7=B7=F1=D2=BB=D6=C2  
            if( pRoot1->m_pElemt != pRoot2->m_pElemt ){  
                flag = false;  
                break;  
            }  
            //=C5=D0=B6=CFpRoot1=BA=CDpRoot2=D7=F3=D3=D2=BD=DA=B5=E3=BD=E1=B9=B9=CA=C7=B7=F1=CF=E0=CD=AC  
            if( ( pRoot1->m_pLeft != NULL &amp;&amp; pRoot2->m_pLeft == NULL )    ||  
                ( pRoot1->m_pLeft == NULL &amp;&amp; pRoot2->m_pLeft != NULL )    ||  
                ( pRoot1->m_pRight != NULL &amp;&amp; pRoot2->m_pRight == NULL )    ||  
                ( pRoot1->m_pRight == NULL &amp;&amp; pRoot2->m_pRight != NULL )  
            ){  
                flag = false;  
                break;  
            }  
   
            //=BD=AB=D7=F3=D3=D2=BD=DA=B5=E3=C8=EB=B6=D3  
            if( pRoot1->m_pLeft != NULL )  
                que1.push( pRoot1->m_pLeft);  
            if( pRoot1->m_pRight != NULL )  
                que1.push( pRoot1->m_pRight);  
            if( pRoot2->m_pLeft != NULL )  
            if( pRoot2->m_pRight != NULL )  
                que2.push( pRoot2->m_pRight);  
        }  
  
  
        if( flag == false )  
            break;  
    }  
  
    //=C8=E7=B9=FB=B1=C8=BD=CF=B1=EA=D6=BE=CE=AAfalse=A3=AC=D4=F2=B2=BB=CF=E0=CD=AC  
    if( flag == false ){  
        while( !que1.empty() )  
            que1.pop();  
        while( !que2.empty())  
            que2.pop();  
  
  
        return false;  
    }  
  
  
    return true;  
}  
