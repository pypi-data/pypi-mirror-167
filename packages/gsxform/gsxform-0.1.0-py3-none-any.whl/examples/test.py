import gsxform
import torch


def create_adj(x: torch.Tensor, p: float = 0.5) -> torch.Tensor:
    """Utility function used to create random a adjacency matrix."""
    return (x > p).float()

def main():
    # input graph, 100 nodes, batch of 16
    g = torch.rand((16, 1000, 1000))
    x = torch.rand((16, 100, 1000))  # batch_size, n_features, n_nodes
    W_adj = create_adj(g)

    # testing variations:
    for jj in [3, 4, 5]:
        for ll in [2, 3, 4]:
            txform = gsxform.scattering.Diffusion(W_adj, jj, ll)
            phi = txform(x)
            #
            assert phi.shape[0:2] == torch.Size([16, 100])

            assert not torch.isnan(phi).any()

if __name__=="__main__":
    # scalene --profile-interval 1 test.py --outfile prof.json --json
    main()

    pass