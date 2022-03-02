#include <iostream>
#include <queue>

using namespace std;

char map[105][105];//地图；
int m,n,ans,fx,fy;
int dir[8][2] = {{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};//8个方向；

void dfs(int x,int y)
{
    int xx,yy;
    for(int i = 0; i < 8; i++){//当前点所有移动的可能；
        xx = x + dir[i][0];
        yy = y + dir[i][1];
        if(xx == fx&&yy == fy){//如果在某次移动后，回到循环起始点，计数器加1；
            ans++;
            map[xx][yy] = '.';//将该点清除，表示该点已被走过，下同；
        }
        if(xx >= 0&&xx < m&&yy >= 0&&yy < n&&map[xx][yy] == '#'){//如果没有回到起始点且
            map[xx][yy] = '.';                                   //满足可移动条件，就继续走；
            dfs(xx,yy);
        }
    }
}

int main()
{
    cin>>m>>n;
    for(int i = 0; i < m; i++){
        cin>>map[i];
    }//输入地图：
    for(int i = 0; i < m; i++){

        for(int j = 0; j < n; j++){
            if(map[i][j] == '#'){//寻找环的起点；
                fx = i;
                fy = j;//标注搜索起始点；
                dfs(i,j);
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}

