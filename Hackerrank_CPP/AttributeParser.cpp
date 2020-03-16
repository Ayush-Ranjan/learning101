#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
struct Node
{
    string key;
    string value;
    Node *next;
};
struct Node* add(Node *head, string k, string v)
{
    if(head==NULL)
    {
        head = (struct Node *) malloc(sizeof(struct Node));
        head->key=k;
        head->value=v;
        head->next=NULL;
        return head;               
    }
    Node *curr=head;
    while(curr->next!=NULL)
    {
        curr=curr->next;
    }
    curr->next = (struct Node*) malloc(sizeof(struct Node)); 
    curr->next->key=k;
    curr->next->value=v;
    curr->next->next=NULL;
    return head;

}
string keyFind(Node *head,string k)
{
   // cout<<head->key<<'\n';
    Node *curr=head;
    while(curr!=NULL)
    {
        //cout<<curr->key<<'\n';
        if(k.compare(curr->key)==0)
        {
            return curr->value;
        }
        curr=curr->next;
    }
    string a="Not Found!";
    return a;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,q;  
    cin>>n>>q;
    Node *ar[n/2];
    string tag[n/2];
    string tagname="";
    for(int x=0,j=0; x<n; x++)
    {
        ar[j]=NULL; 
        string s;
        string prev;
        string k;
        char ch=' ';
        string inp;
        cin>>inp;
        inp.erase(0,1);
        if(inp.at(0)!='/'||inp.at(inp.length()-1)!='>')
        {
            if(inp.at(inp.length()-1)=='>')
            {
                tagname=tagname+'.'+inp.erase(inp.length()-1);
                ar[j]=add(ar[j]," "," ");
            }
            else
            {
            tagname=tagname+"."+inp;
            //cout<<tagname<<'\n';
            do
            {
                cin>>s;
                //cout<<s<<'\n';
                if(ch=='=')
                {
                    ch=s.at(s.length()-1);
                    //cout<<ch<<'\n';
                    int l=s.find('\"');
                    //cout<<l<<'\n';
                    s=s.erase(l,l+1);
                    s=s.erase(s.find('\"',l+1));
                    //cout<<k<<s<<'\n';
                    ar[j]=add(ar[j],k,s);
                }
                else
                {
                    ch=s.at(s.length()-1);
                    //cout<<ch<<'\n';
                }
                if(ch=='=')
                {
                    k=prev;
                    //cout<<k<<'\n';
                }
                prev=s;
            }while(ch!='>');
            }
            tag[j]=tagname;
            j++;
        }
        else
        {
            for(int i=tagname.length()-1;i>=0;i--)
            {
                if(tagname.at(i)=='.')
                {
                    tagname=tagname.erase(i);
                    break;
                }
            }
            
        }
    }
    //cout<<keyFind(ar[0],"name")<<'\n';
    for(int x=0; x<q; x++)
    {
        string s;
        string tf;
        int count=0;
        bool flag=false;
        cin>>s;
        //cout<<s<<'\n';
        size_t find=s.find('~');
        tf='.'+s.substr(0,find);
       // cout<<tf<<'\n';
        for(int y=0; y<n/2; y++)
        {
            if(tf.compare(tag[y])==0)
            {
                count=y;
                flag=true;
                break;
            }
        }
        //cout<<count<<'\n';
        if(flag==true)
        {
            //cout<<count;
            string a=s.substr(find+1);
            //cout<<a<<'\n';
            string b=keyFind(ar[count],a);
            cout<<b<<'\n';
        }
        else
        cout<<"Not Found!"<<'\n';
    }
    return 0;
}
