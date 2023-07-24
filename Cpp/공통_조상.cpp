#include <iostream>
#include <vector>

using namespace std;

struct Node // 노드 vetcor 할당????
{
    vector<int> chidren;
    int parents;

    Node() : parents(0) {}
}

int ans, N, M, A, B;
Node* nodes;
vector<int> ancestorA, ancestorB;

void traverse(int idx, vector<int>& ancestor) {
    int parent = nodes[idx].parents; //조상 찾는 재귀함수
    if (parent != 0) {
        traverse(parent, ancestor);
    }
}

int dfs(int idx) {
    int res = 1;
    for (int child : nodes[idx].children) {
        res += dfs(child);
    }
}

int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T, t++) {
        cin >> N >> M >> A >> B; // 입력 받기 
        nods = new Node[N+1];
        ancestorA.clear();
        ancestorB.clear();

        for ( int i = 0; i< M; i ++) {
            int p, c;
            cin >> p >> c;
            nodes[p].children.push_back(c);
            nodes[c].parents = p ;
        }

        traverse(A, ancestorA); // 부모 조상 찾기 
        traverse(B, ancestorB);

        for (int i = 0; i< N; i++) {
            if (ancestorA[i] != ancestorB[i]) break;
            ans = ancestorA[i];
        }
            // 입력 받기
            cout << "#" << t << " " << ans << " " << dfs(ans)
            endl;

            delete[] nodes;
    }
    return 0

}
